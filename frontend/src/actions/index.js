export function selectRestaurantTab(tab) {
	return{
		type:'TAB_SELECTED',
		payload:tab
	};
}

// export function addReview(review){
// 	return{
// 		type:'ADD_REVIEW',
// 		payload:review
// 	};
// }

// export function fetchReview(review){
// 	return{
// 		type:'FETCH_REVIEW',
// 		payload:review
// 	}
// }

// export function addReply(reply){
// 	return{
// 		type:'ADD_REVIEW',
// 		payload:reply
// 	}
// }

// export function fetchReview(reply){
// 	return{
// 		type:'FETCH_REVIEW',
// 		payload:reply
// 	}
// }