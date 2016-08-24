import React, { Component } from 'react';
import _ from 'lodash';

export default class OverviewDetail extends Component {
	constructor(props){
		super(props);
	}
	render() {
		console.log('this.props.data',this.props.data);
		return (
			<div>
				<p>is he authenticated?</p>
				{this.props.data.count_favorite}
			</div>
		);
	}
}
