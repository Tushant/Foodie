import React, { Component } from 'react';
import { connect } from 'react-redux'; // switches component to container so that it has direction interaction with state
import { selectRestaurantTab } from '../actions/index';
import { bindActionCreators } from 'redux'; // action flows up now to all the reducers
import _ from 'lodash';

export default class RestaurantTabList extends Component {
	renderList(){
		return _.map(this.props.restaurantTab, ( tab ) => {
			return(
					  <a className="item" key={ tab.id } onClick = { () => this.props.selectRestaurantTab(tab) }>
					   { tab.title }
					  </a>
				);
		});
	}
	render() {
		return (
			<div className="tab-menu">
				<div className="ui secondary pointing menu">
					{this.renderList()}
				</div>
			</div>
			
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