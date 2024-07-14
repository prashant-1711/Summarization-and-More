import React from "react";
import { FaGithub, FaLinkedin, FaInstagram } from 'react-icons/fa';

function Footer() {
  return (
    <footer className="footer">
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <h4>Connect with Us</h4>
            <ul className="list-inline">
              <li className="list-inline-item">
                <a className="social-link" href="www.github.com/prashant-1711" target="_blank" rel="noopener noreferrer">
                  <FaGithub size="3em"/>
                  
                </a>
              </li>
              <li className="list-inline-item">
                <a className="social-link" href="https://www.linkedin.com/in/prashant-mohite-9880a3207/" target="_blank" rel="noopener noreferrer">
                  <FaLinkedin size="3em"/>
                </a>
              </li>

            </ul>
          </div>
          <div className="col-md-6">
            <h4>Contact Us</h4>
            <p>Email: <a href="mailto:tcad1704@gmail.com">tcad1704@gmail.com</a></p>
    
          </div>
        </div>
        
      </div>
    </footer>
  );
}

export default Footer;
