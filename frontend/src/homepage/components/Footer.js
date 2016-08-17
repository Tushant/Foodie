import React from 'react';

export default class Footer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      advanceSearch:false,
      display:true,
    }
  }

  handleChange (event) {
    this.setState({
        advanceSearch:!this.state.advanceSearch,
        display:!this.state.display
    });
  }

  render() {
        var styling = { color: '#fff' };
        var hidingNonAdvanceSearch = { display : this.state.display ? 'block' : 'none' };
        return (
            <div className="content-footer">
            <div className="container">
                <div className="row text-center">
                    <div className="col-sm-12">
                        <div>
                            <div className = "row">
                             <div className = "col-sm-12 col-md-4"></div>
                                <div className = "col-sm-12 col-md-4"style = { hidingNonAdvanceSearch }>
                                <form method="GET" action="/search/" className = "form-inline" >
                                    <div className = "input-group">
                                        <input id="location" type="textbox" className = "form-control" name="landmark" required autocomplete="off" placeholder = "name of the place" />
                                            <div className = "input-group-btn">
                                                <button className = "btn btn-primary find" type = "submit" value = "find" name="findspace">Find Space
                                                </button>
                                            </div>
                                    </div>
                                    <br/>
                                </form>
                                </div>
                                <div className = "col-sm-12 col-md-4"></div>
                            </div>
                            <div className = "row" >
                                <div className="form-group checkbox" style={styling}>
                                        <label className="checkbox-inline lead">
                                         <input type="checkbox" value="option1" onChange={this.handleChange.bind(this)} /> Advance Search
                                        </label>
                                    { this.state.advanceSearch ?  <AdvanceSearchBox /> : null }
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            </div>
            );
    }
}

class AdvanceSearchBox extends React.Component{
  render(){
    return(
            <div className="container">
            <div className = "row text-center" >
                <div className = "col-sm-12" >
                 <form method="GET" action="/search/" className = "form-inline" >
                    <div className = "input-group">
                        <input id="location" type="textbox"  className = "form-control" name="landmark" required autocomplete="off" placeholder = "name of the place" />
                            <div className = "input-group-btn">
                                <select className = "form-control" name="Bedrooms">
                                    <option>1 room</option>
                                    <option>2 rooms</option>
                                    <option>3 rooms</option>
                                    <option>4 rooms</option>
                                    <option>5 rooms</option>
                                    <option>6 rooms</option>
                                    <option>7 rooms</option>
                                    <option>8 rooms</option>
                                    <option>8+ rooms</option>
                                </select>
                            </div>
                            <div className = "input-group-btn">
                                <button className = "btn btn-primary find" type = "submit" value = "find" name="findspace">Find Space
                                </button>
                            </div>
                    </div>
                </form>
                </div>
            </div>
            </div>
          );
  }
}
