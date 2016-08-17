import React from 'react';
import ReactDOM from 'react-dom';
import LoginModal from 'homepage/LoginModal';

window.app = {

    showLoginModal: function(id,data){
        ReactDOM.render(
          <LoginModal data={data} />, document.getElementById(id)
        );
    },
}