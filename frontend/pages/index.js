import React, {useEffect} from 'react';
import Link from 'next/link';
import Head from 'next/head';
import { useDispatch, useSelector } from 'react-redux';
// import {LOG_IN, LOG_OUT} from '../reducers/user';
import {loginAction, logoutAction} from '../reducers/user';
import LoginForm from '../components/LoginForm';

const Home = () => {
  const dispatch = useDispatch();
  // const {isLoggedIn, user} = useSelector(state => state.user)
  const user = useSelector(state => state.user.user)
  const isLoggedIn = useSelector(state => state.user.isLoggedIn)
  const {mainGroups} = useSelector(state => state.group)
  console.log(isLoggedIn)
  console.log(user)

  return (
    <div className="index">
      <nav>
        <span className="logo"><Link href="/"><a>Logo</a></Link></span>
        <span className="linkBtn-container">
          <li className="linkBtn"><Link href=""><a>linkBtn</a></Link></li>
          <li className="linkBtn"><Link href="/dashboard"><a>dashboard</a></Link></li>
          <li className="linkBtn"><Link href=""><a>
            {/* {dummy.isLoggedIn ? 'LOGOUT' : 'LOGIN' } */}
            </a></Link></li>
          {user ? <div>로그인했습니다. {user.nickname}</div> : <div>로그아웃 했습니다</div>}
        </span>
        
        <span className="profile"><Link href="/profile"><a>profile</a></Link></span>
      </nav>
      <LoginForm/>
      <section className="main">
        {/* main */}
        <article>
          <div>Welcome!</div>
          <div>
            Maxturn - 수익률을 확인하고 투자하세요.
            <br></br>
            맥스턴은 백테스트를 진행하고, 이에 대한 전략을 수립하고 유저들과 공유하는 플랫폼입니다.
          </div>
          <div>
            맥스턴은 여러분의 시간, 노력을 절감시켜줄 수 있습니다.
          </div>
        </article>
      </section>

      <section className="introduction">
        {/* introduction */}
        <div className="introduction_title">INTRODUCTION</div>
        <article>
          <div>
            <figure>photo</figure>
            <figcaption>설명</figcaption>
          </div>
        </article>

        {/* <Pagination/> */}

        {/* <article>
          <figure>photo</figure>
          <figcaption>설명</figcaption>
        </article>
        <article>
          <figure>photo</figure>
          <figcaption>설명</figcaption>
        </article> */}
      </section>

      <section className="login">
        {/* 로그인 */}
        <article>
          <form>
            <div>Log in to your account</div>
            <div className="idBox">
              <label for="user_id">Username</label>
              <input type="text" id="user_id"></input>
            </div>
            <div className="pwBox">
              <label for="user_password">Password</label>
              <input type="password"></input>
            </div>
            <button type="submit"></button>
          </form>
        </article>
      </section>
      <footer>

      </footer>
    </div>
  );
};

export default Home;