import React from 'react';
import ReactDOM from 'react-dom';
import SearchInput, {createFilter} from 'react-search-input';
import Request from 'superagent';
import _ from 'lodash';

export default class Body extends React.Component {

  constructor(props) {
    super(props);
    this.state = { };
    this.handleClick = this.handleClick.bind(this);
    this.handleKeyDown = this.handleKeyDown.bind(this);
    this.searchUpdated = this.searchUpdated.bind(this);
  }

  handleClick(e){
    var mySearch = document.getElementById('mySearch');

    if (ReactDOM.findDOMNode(mySearch).style.visibility == 'visible')
    {
      ReactDOM.findDOMNode(mySearch).style.visibility = 'hidden';
      ReactDOM.findDOMNode(mySearch).style.opacity = '0';
    }
    else
    {
      ReactDOM.findDOMNode(mySearch).style.visibility = 'visible';
      ReactDOM.findDOMNode(mySearch).style.opacity = '1';
    }

  }


  handleKeyDown(e){
    if (e.keyCode == 27) {
      this.handleClick();
    }
  }

  componentWillMount(){
  	this.search();
  }

  search( query='place' ){
  	let url = "http://localhost:8000/api/v1/rental/?place__startswith="+encodeURIComponent(query);
  	Request.get(url).then((response) => {
  		console.log('response',response.body.objects);
  		this.setState({
  			place:response.body.objects,
  		});
  		console.log('this.state.place',this.state.place);
  	});
  }

  searchUpdated(term){
  	console.log('term is',term);
  	this.search(term);
  }

  render() {
        var margin = { marginTop : '13em' };
        let location = _.map(this.state.place, (place,id) => {
        	return(
        			<div className="searchResult">
        				<a href={ "/rent/" + place.slug }><h3>{place.place}</h3></a>
        			</div>
        		)
        });
        let gallery = _.map(this.state.place, (place,id) => {
        	console.log('place',place.gallery);
        	_.map(place.gallery, (image,id) => {
        		return(
        				<img src={image.image} class="img-fluid" />
        			)
        	});
        });
        return(
            <div className = "container">
                <div className="content text-align-center">
                    <div className="row text-xs-center">
                        <div className="middle-text"  style={margin}>
                            <h1 className="welcome"><span>Rental Space Welcome's you </span></h1>
                            <button ref="test" className="btn how-it-works" onClick={this.handleClick}>Search Space</button>
                        </div>
                    </div>
                </div>
                <div id="mySearch" className="overlay"  onKeyDown={this.handleKeyDown}>
                  <button className="btn closebtn" onClick={this.handleClick}>x</button>
                  <div className="overlay-content">
                        <SearchInput ref="searchInput" className="search-input" onChange={this.searchUpdated} />
                        <ul>{location}</ul>
                  </div>
            </div>
            </div>
            );
    }
}

