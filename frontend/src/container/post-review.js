import React, { Component } from 'react';
import { reduxForm } from 'redux-form';
import _ from 'lodash';


class PostReview extends Component{
	onSubmit(props){
		console.log('props',props);
		axios.post('/user', {
	    review: props.review
	  })
	  .then(function (response) {
	    console.log(response);
	  })
	  .catch(function (error) {
	    console.log(error);
	  });
	}
	
	render(){
	const { fields : { review }, handleSubmit } = this.props; 
	return(
		<form onSubmit={ handleSubmit(props => this.onSubmit(props))}>
			<div className={`form-group ${review.touched && review.invalid ? 'has-danger' : ' ' }`}>
				<input type="text" className="form-control" {...review} />
				<div className="text-help">
					{review.touched ? review.error : '' }
				</div>
			</div>
			<button type="submit" className="btn tomato">Pen your review</button>
		</form>
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

export default reduxForm({
	form:'PostReview',
	fields:['review'],
	validate
})(PostReview);