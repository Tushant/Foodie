// state argument is not an application state, only the state this reducer is responsible for
export default function(state = null, action){
	switch(action.type){
		case 'TAB_SELECTED':
			return action.payload;
	}

	return state;

}