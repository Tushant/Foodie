// state argument is not an application state, only the state this reducer is responsible for
export default function(state = null, action){
	console.log('state',state);
	switch(action.type){
		case 'TAB_SELECTED':
			console.log('action.payload of clicked tab is',action.payload);
			return action.payload;
	}

	return state;

}