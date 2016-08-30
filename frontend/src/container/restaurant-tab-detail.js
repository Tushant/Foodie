import React, { Component } from 'react';
import { connect } from 'react-redux';
import _ from 'lodash';

import OverviewDetail from './overview-detail';
import MenuDetail from './menu-detail';
import PostReview from './post-review';

class RestaurantTabDetail extends Component {
	constructor(props){
		super(props);
	}

	render() {
		const { data, restaurantTabActive } = this.props;
		if (!restaurantTabActive ){
			return ( <OverviewDetail data={data}/> );
		}
		
		if(restaurantTabActive.title=='Overview'){
			return ( <OverviewDetail data={data}/> );
		}

		if(restaurantTabActive.title=='Menu'){
			return ( <MenuDetail data={data}/> );
		}

		if(restaurantTabActive.title=='Write a Review'){
			return ( <PostReview data={data}/> );
		}
	}
}


function mapStateToProps(state){
	return{
		restaurantTabActive: state.restaurantTabActive
	};
}

export default connect(mapStateToProps)(RestaurantTabDetail);
