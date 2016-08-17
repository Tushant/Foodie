import React from 'react';

export default class Navbar extends React.Component {
  render() {
    console.log(this.props.data);
    var userIcon = this.props.data.isUserAuthenticated ? 
    <span className="text-muted"><a href="/accounts/logout/"><span className="glyphicon glyphicon-user"></span>  Sign out</a></span> :
    <span className="text-muted"><a href="/accounts/login/"><span className="glyphicon glyphicon-user"></span>Sign In</a></span>;
    return (
         <div className="Navigation">
	         <div className="collapse" id="exCollapsingNavbar">
			  <div className="bg-inverse p-a-1 collapseBar">

			    <span className="text-muted"><a href="/">Home</a></span>
			    <span className="text-muted"><a href="/add/">Add Rent</a></span>
			    <span className="text-muted"><a href="/roomlist/">Room List</a></span>
			    {userIcon}
			  </div>
			</div>
			<nav className="navbar navbar-light bg-faded navbg">
			  <button className="navbar-toggler pull-right hamburger" type="button" data-toggle="collapse" data-target="#exCollapsingNavbar">
			    &#9776;
			  </button>
			  <a href="/" className="logo pull-left"><img src="/static/img/CRSLogoWhite.png" /></a>
			</nav>
		</div>
    );
  }
}
