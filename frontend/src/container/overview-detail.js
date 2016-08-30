import React, { Component } from 'react';
import axios from 'axios';
import _ from 'lodash';

export default class OverviewDetail extends Component {
	constructor(props){
		super(props);
		this.state = { restaurant : [] }
	}

	componentDidMount(){
        this.loadRoomFromServer();
    }

    loadRoomFromServer(){
    	axios({
			method:'GET',
			url:`/api/restaurant/${this.props.data.slug}`,
		})
		.then(response => {
			console.log(response.data);
			this.setState({
				restaurant:response.data
			});
		})
		.catch(error => {
			console.log(error);
		});
    }

    renderFeatures(){
			return _.map( this.state.restaurant.features, (feature) => {
				return(
						<li key={feature.id} className="list-item">
							{feature.features}
						</li>
					)
			})
		}

	render() {
		const { restaurant } = this.state;
		return (
			<div>
				<h1 className="center">{restaurant.name}</h1>
				<div className="col-sm-12 col-md-4">
					City:{restaurant.city}<br/>
					Address:{restaurant.address}<br/>
					Phone number:{restaurant.address}<br/>
				</div>
				<div className="col-sm-12 col-md-6">
					Owner email:{restaurant.owner_email}<br/>
					Owner:{restaurant.owner}<br/>
					Features:{this.renderFeatures()}
				</div>
			</div>
		);
	}
}
