import React from 'react';
import {Link} from "react-router-dom";
import BannerImage from '../assets/thefirst.webp';
import '../styles/Home2.css';
import WorldImage from '../assets/theworld.webp';
import GestureImage from '../assets/gesture.png';
import AiImage from '../assets/aipic.png';
import CommImage from '../assets/communicationpic.png';

function Home() {
  return (
    <div className="home" >
        <div className='body'>
        <div className="upperBody" style={{ backgroundImage: `url(${BannerImage})` }}>
            <div className="headerContainer">
                <h1>Gesture Genius</h1>
                <p>Merging the Deaf and Hearing Communities</p>
                <Link to="/menu">
                    <button> Try Now! </button>
                </Link>
            </div>
        </div>
        <div className="lowerBody">
            <section class="info-section">
                <img src={WorldImage} className ='left-image' />  
                <div class="text-content">
                    <h2>70 Million People</h2>
                    <p>Just in the United States, 11 million people are deaf, of which half a million use ASL natively.</p>
                    <p>For people who are deaf to communicate with those who are hearing, and therefore most likely not fluent in sign language, they’re constricted to slower methods of communication, such as writing. Similarly, for people who don’t know sign language to immediately be able to communicate comfortably with someone who is deaf, the only options are writing or lip-reading, which has been proven to only be 30-40% effective. By creating GestureGenius, we aim to make the day to day lives of both the deaf and hearing communities significantly more tension-free. </p>
                </div>
            </section>
        
            <hr />
        
            <section class="images-section">
                <div class="image-container">
                    <img src={GestureImage} />
                    <p class="caption">Gesture Recognition: Our most impressive development was allowing for gesture/action recognition rather than simply finger spelling. Nearly all existing applications have in-built functions only to recognize individual, static letters, while the majority of words in ASL are separate actions.</p>
                </div>
                <div class="image-container">
                    <img src={CommImage} />
                    <p class="caption">Two-Way communication: We not only have created a sign-language to text translator to help deaf people communicate, but we have developed a text to sign-language translator to allow deaf people to “hear” the words that others are saying more effectively. </p>
                </div>
                <div class="image-container">
                    <img src={AiImage} />
                    <p class="caption">Mediapipe Usage: Our model uses a highly tested and high accuracy hand motion recognition model developed by Google: Mediapipe, making our models extremely capable at various, often-overlooked tasks such as hand differentiation.</p>
                </div>
            </section>
        </div>
        </div>
    </div>
  )
}

export default Home
