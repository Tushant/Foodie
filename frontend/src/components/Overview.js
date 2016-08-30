import React from 'react';
import { Component } from 'react';
import RestaurantTabList from '../container/restaurant-tab-list';
import RestaurantTabDetail from '../container/restaurant-tab-detail';

export default class Overview extends Component{
  render(){
  const marginTop = { marginTop:'100px', background:'rgba(230, 230, 230, 0.61)', paddingBottom:'7em'};
   return(
      <div className="App">
        <div className="container-fluid" style={marginTop}>
          <div className="row">
            <div className="col-md-12">
              <RestaurantTabList />
            </div>
            <div className="col-md-12">
             <RestaurantTabDetail data={this.props.data} />
            </div>
          </div>
        </div>
      </div>
      );
  }
}