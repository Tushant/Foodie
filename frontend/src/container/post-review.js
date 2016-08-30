import React, { Component, PropTypes } from 'react';
import { reduxForm } from 'redux-form';
import $ from 'jquery';
import axios from 'axios';
import _ from 'lodash';


class PostReview extends Component{
	constructor(props){
		super(props);
		this.state = { reviewByUser: [], wantToReply: false }
		this.handleReplySubmit = this.handleReplySubmit.bind(this);
	}
	loadReviewFromServer(){
		axios({
			method:'GET',
			url:`/api/restaurant/${this.props.data.slug}`
		})
		.then(response => {
			this.setState({
				reviewByUser:response.data.review
			})
		})
		.catch(error => {
			console.log(error);
		});
	}
	componentDidMount() {
		this.loadReviewFromServer();
	}
	onSubmit(props){
		axios({
			method:'POST',
			url:`/api/review/create/?type=restaurant&slug=${this.props.data.slug}`,
			headers:{
				'X-CSRFToken':CSRF_TOKEN,
				'Access-Control-Allow-Origin':'*',
				'Accept': 'application/json',
    			'Content-Type': 'application/json',
			},
			data:{
				review:props.review
			}
		})
		.then(response => {
			this.loadReviewFromServer();
		})
		.catch(error => {
			throw("Error: ",error);
		});
	}

	handleReplySubmit(event){
		console.log(event.target)
		// const id = $(event.target).data("review-click-id");
		this.setState({
			wantToReply:!this.state.wantToReply
		});
	}


	renderAllReview(){
		return _.map(this.state.reviewByUser, (review) => {
			return (
				<div className="contents" key={review.id}> 
					<a className="author">{ review.reviewer }</a>
				    <div className="metadata">
				        <span className="date">Today at 5:42PM</span>
				    </div>
				    <div className="text">
				        { review.review }
				    </div>
				    <div className="actions">
				        <a className="reply" data-review-click-id={review.id} onClick={this.handleReplySubmit}>Reply</a>
				    </div>
				   {this.renderAllReply(review)}

				</div>
				)
		});
	}

	renderAllReply(review){
		return _.map(review.children, (reply) => {
			return(
					 <div className="content" key={reply.id}>
					          <a className="author">{reply.reviewer}</a>
					          <div className="metadata">
					            <span className="date">Just now</span>
					          </div>
					          <div className="text">
					            {reply.review}
					          </div>
					  </div>
				)
		})
	}
	render(){
	const { fields : { review }, handleSubmit } = this.props; 
	return(
		<div className="review-section">
			<form onSubmit={ handleSubmit(props => this.onSubmit(props))} className="form-inline">
				<div className={`form-group ${review.touched && review.invalid ? 'has-danger' : ' ' }`}>
					<input type="text" className="form-control" {...review} />
					<div className="text-help">
						{review.touched ? review.error : '' }
					</div>
				</div>
				<button type="submit" className="btn tomato">Pen your review</button>
			</form>
			<div className="all-reviews">
				<div className="ui comments">
					<h3 className="ui dividing header">Reviews</h3>
					<div className="comment">
						<div className="content">
							{ this.renderAllReview() }
						</div>
					</div>
				</div>
			</div>
		</div>
	)
	}
}

function validate(values){
	const errors = {};

	if(!values.review){
		errors.review = 'Enter Review';	
	}
	return errors;
}

PostReview.propTypes = {
    fields: PropTypes.object.isRequired,
    handleSubmit: PropTypes.func.isRequired,
    submitting: PropTypes.bool.isRequired
}

export default reduxForm({
	form:'PostReview',
	fields:['review'],
	validate
})(PostReview);

