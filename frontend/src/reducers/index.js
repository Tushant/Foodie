import { combineReducers } from 'redux';
import RestaurantTabReducerList from './reducer-restaurant-tab-list.js';
import RestaurantTabReducerActive from './reducer-restaurant-tab-active.js';
import {reducer as formReducer} from 'redux-form';

const rootReducer = combineReducers({
	restaurantTab:RestaurantTabReducerList, // restaurantTab is a state
	restaurantTabActive:RestaurantTabReducerActive,// will have the value of action.payload whenever action will be triggered
	form:formReducer
});

export default rootReducer;