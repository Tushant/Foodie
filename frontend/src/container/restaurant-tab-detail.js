import React, { Component } from 'react';
import { connect } from 'react-redux';
import _ from 'lodash';

import OverviewDetail from './overview-detail';
import PostReview from './post-review';

class RestaurantTabDetail extends Component {
	constructor(props){
		super(props);
	}
	render() {
		if (!this.props.restaurantTabActive ){
			return ( <OverviewDetail data={this.props.data}/> );
		}
		return (
			<div>
				<h1 className="lead"><PostReview /></h1>
			</div>
		);
	}
}


function mapStateToProps(state){
	return{
		restaurantTabActive: state.restaurantTabActive
	};
}

export default connect(mapStateToProps)(RestaurantTabDetail);
