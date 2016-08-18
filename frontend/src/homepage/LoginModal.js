import React, { Component } from 'react';
import $ from 'jquery';
// import Footer from './components/Footer';
// import { Router, Route, IndexRoute, hashHistory } from 'react-router';

class LoginModal extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			showModal:'none'
		}
	}

	componentDidMount() {
	
		// $('.ui.modal').modal({detachable: false});
		console.log('hello');
		// console.log('addLoginModalevent',this.AddLoginModalEvent());
	}

	showModal(){
		this.setState({ showModal:'inherit' });
		 // $('.ui.modal.editform').modal('show');
	}

	closeModal(){
		this.setState({ showModal:'none'});
	}

  render() {
  	console.log("Render");
  	const style = { display:this.state.showModal, top:'50px' };
  	const close = <div className="ui black deny button" onClick={this.closeModal}> Nope </div>;
    return (
          <div>
          	<AddLoginModal style={style} title="Login" close={close} />
          </div>
      )
  }
}
 

class AddLoginModal extends Component{
	render(){
		return(
				<div style={this.props.style}>
		            <div className="ui modal editform">
		                <div className="ui middle aligned center aligned grid">
						  <div className="column">
						    <h2 className="ui teal image header">
						      <div className="content">
						        Log-in to your account
						      </div>
						    </h2>
						    <form className="ui large form">
						      <div className="ui stacked segment">
						        <div className="field">
						          <div className="ui left icon input">
						            <i className="user icon"></i>
						            <input type="text" name="email" placeholder="E-mail address" />
						          </div>
						        </div>
						        <div className="field">
						          <div className="ui left icon input">
						            <i className="lock icon"></i>
						            <input type="password" name="password" placeholder="Password" />
						          </div>
						        </div>
						        <div className="ui fluid large teal submit button">Login</div>
						      </div>

						      <div className="ui error message"></div>

						    </form>

						    <div className="ui message">
						      New to us? <a href="#">Sign Up</a>
						    </div>
						  </div>
						</div>
		            </div>
        		</div>
			)
	}
}

export default LoginModal;



