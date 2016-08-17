import React from 'react';
import ReactDOM from 'react-dom';
import SearchInput, {createFilter} from 'react-search-input';
import Request from 'superagent';
import _ from 'lodash';

export default class Body extends React.Component {

  constructor(props) {
    super(props);
    this.state = {place:[]};
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
  	let url = "/api/rentals/?q="+encodeURIComponent(query);
    console.log('url is', url);
  	Request.get(url).then((response) => {
      console.log('response',response);
    if (response) {
        this.setState({
            place:response.body.results,
        });
    } else {
        this.setState({
            place: [],
        });
    }
});

  }

  searchUpdated(term){
  	this.search(term);
  }

  render() {
        var margin = { marginTop : '13em' };
        console.log(this.state.place);
        if (this.state.place){
        let location = _.map(this.state.place, (place,id) => {
        	return(
        			<Room key={id}
              pk = {place.id}
        			slug={place.slug}
        			place={place.place}
        			city={place.city}
        			gallery={place.gallery}
        			property={place.property}/>
        		)
        });
        let gallery = _.map(this.state.place, (place,id) => {
        	_.map(place.gallery, (image,id) => {
        		return(
        				<img src={image.image} class="img-fluid" />
        			)
        	});
        });
        let noLocation = () => {
          return(
            <div className="col-md-6 col-md-offset-3 col-xs-12">
              <img src="/static/img/noRentFound.png" className="img-fluid" />
            </div>
          );
        };

        return(
            <div className = "container">
                <div className="content text-align-center">
                    <div className="row text-xs-center">
                        <div className="middle-text"  style={margin}>
                            <h1 className="welcome"><span>Common Rent Space</span></h1>
                            <p className="appSubtitle">Facilitates your search for rent space all over 
Nepal</p>
                            <button ref="test" className="btn how-it-works" onClick={this.handleClick}>Search Space</button>
                        </div>
                    </div>
                </div>
                <div id="mySearch" className="overlay" onKeyDown={this.handleKeyDown}>
                  <button className="btn closebtn" onClick={this.handleClick}>x</button>
                  <div className="overlay-content">
                        <SearchInput ref="searchInput" className="search-input" onChange={this.searchUpdated} />
                         <div className="container searchList">
	                       { this.state.place.length >=1 ? location : noLocation() }
	                	</div>
                  </div>
            </div>
            </div>
            );
    }
    }
}

class Room extends React.Component{
	render(){
		let imageFile = _.map(this.props.gallery, (image) => {
            return(
                    <img src={image.image} className="img-fluid" width="250px" height="250px" />
                );
        });
		return(
                <div className="room">
                	 <div className="thumbnail">
                        { imageFile[0] }
                    </div>
                    <h3 className="listingName text-left">
                     <a href = { "/rent/" + this.props.pk }>{this.props.place}</a>
                    </h3>
                    <span className="propertySpan">
                        <i className = "fa fa-home"></i>
                        <span className="property">{this.props.property}</span>
                    </span>
                </div>
            )
	}
}
