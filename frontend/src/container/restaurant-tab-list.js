import React, { Component } from 'react';
import { connect } from 'react-redux'; // switches component to container so that it has direction interaction with state
import { selectRestaurantTab } from '../actions/index';
import { bindActionCreators } from 'redux'; // action flows up now to all the reducers
import _ from 'lodash';

export default class RestaurantTabList extends Component {
	renderList(){
		return _.map(this.props.restaurantTab, ( tab ) => {
			console.log('tab',tab);
			return(
					<li 
						key = { tab.id } 
						onClick = { () => this.props.selectRestaurantTab(tab) }
						className="list-group-item tab-menu">
						{ tab.title }
					</li>
				);
		});
	}
	render() {
		return (
			<ul className="list-group col-sm-4">
				{this.renderList()}  {/* it is a helper function */}
			</ul>
		);
	}
}

function mapStateToProps(state){
	return{
		restaurantTab:state.restaurantTab
		// restaurantTabActive
	};
}

function mapDispatchToProps(dispatch){
	return bindActionCreators({ selectRestaurantTab:selectRestaurantTab }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(RestaurantTabList);