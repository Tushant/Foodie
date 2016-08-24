import React, { Component } from 'react';
import $ from 'jquery';

class RestaurantDetail extends Component {
	constructor(props){
		super(props);
		this.state = {
			showForm:false
		}
		this.handleClick = this.handleClick.bind(this);
		this.handleReviewClick = this.handleReviewClick.bind(this);
	}

	handleReviewClick(){
		this.setState({showForm:!this.state.showForm})
	}


	handleClick(e){
		var restaurant = $(e.target).closest(".review-section");
	    console.log(restaurant);
	    var type  = e.target.value;
	    console.log('type',type);
	    var id  = $(e.target).data("restaurant-id");
	    console.log('id',id);
	               function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');
        function csrfSafeMethod(method) {
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
	     $.ajax({
	                type: "POST",
	                url: this.props.data.url,
	                data: {
	                    'type': type,
	                    'id': id
	                    },
	                success: function(response) {
	                   var count_favorite = restaurant.find("#favorite-count-"+id).html(response.favorite_count);
	                   var message = restaurant.find('.message').html('Thansk for giving your heart to us! We love you too.')
	                    console.log(count_favorite);
	                },
		          }); 
	}
	render() {
		return (
			<div className="detail-part">
				<div className="container review-section">
					<div className="row">
						<div className="col-sm-12 col-md-4">
							<form action="" method='post' className="card-link">
								<p className="right">
									<span className="rating">
									<input type="radio" name="vote" className="rating-input" value="favorite" 
										   id={"favorite-"+this.props.data.res_id} data-restaurant-id={this.props.data.res_id} 
										   onClick={this.handleClick} />
									<label htmlFor={"favorite-"+this.props.data.res_id} className="rating-star"><i className="fa fa-heart-o"></i></label>
	                				<span id={"favorite-count-"+this.props.data.res_pk} >{this.props.data.count_favorite}</span>
									</span>
								</p>
							</form>
						</div>
					</div>
					<div className="col-sm-12 col-md-4">
						<AddReview onClick={this.handleReviewClick} showOrNot={this.state.showForm}/>
					</div>
				</div>
			</div>
		);
	}
}


class AddReview extends Component{
	constructor(props){
		super(props);
	}

	render(){
		return(
				<div className="add-review">
					<p onClick={this.props.onClick}>Write Review</p>
					{this.props.showOrNot ? <ReviewForm /> : null}
				</div>
			)
	}
}

class ReviewForm extends Component{
	constructor(props){
		super(props);
	}
	render(){
		return(
				<form action="" method="post" className="form-inline">
					<div className="form-group col-sm-10 col-md-10">
					    <input type="text" className="form-control" id="review" placeholder="write a review" />
				  </div>
				 	 	<button type="submit" className="btn tomato">Pen your review</button>
				</form>
			)
	}
}


export default RestaurantDetail;