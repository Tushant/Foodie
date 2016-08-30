import React, { Component } from 'react';
import axios from 'axios';
import _ from 'lodash';

export default class OverviewDetail extends Component {
	constructor(props){
		super(props);
		this.state = { menu : [] }
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
				menu:response.data.menu
			});
		})
		.catch(error => {
			console.log(error);
		});
    }

	render() {
		const { menu } = this.state;
		console.log('menus are',menu);
		const menu_data = _.map(menu, (menu) => {
			return(
				<div>
					<MenuItem key={menu.id}
							  name={menu.name}
							  price={menu.price}
							  description={menu.description}
							  category={menu.menu_category}/>
				</div>
				);
		});
		return (
			<div>
				<h1>{menu.name}</h1>
				<div className="col-sm-12 col-md-4">
					{menu_data}
				</div>
			</div>
		);
	}
}

class MenuItem extends Component {
	constructor(props){
		super(props);
	}
	render(){
		const {name, price, description, category } = this.props;
		return(
				<div className="menu-item">
					Item:{name}<hr/>
					Description:{description}<hr/>
					Price:{price}<hr/>
				</div>
			)
	}
}