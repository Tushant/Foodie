import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';

import Overview from 'components/Overview';
import reducers from './reducers';

const createStoreWithMiddleware = applyMiddleware()(createStore);

window.app = {
    showDetailRestaurant: function(id,data){
		ReactDOM.render(
		  <Provider store={createStoreWithMiddleware(reducers)}>
		    <Overview data={data} />
		  </Provider>
		  , document.getElementById(id));
	},

}

