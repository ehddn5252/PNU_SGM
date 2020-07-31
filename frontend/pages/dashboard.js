import React from 'react';
import Link from 'next/link';
import MainGraph from '../components/MainGraph';
import SubGraph from '../components/SubGraph';
import Filter from '../components/Filter';

const Dashboard = () => {
  return (
    <div className="dashboard">
      <nav>
        <span className="logo">Logo</span>
        <span className="profile">Photo</span>
        <span className="menuBtn">menu</span>
      </nav>
      <aside>???</aside>
      <section>
        <article className="graphContainer">
          <SubGraph className="subgraph" no="1"/>
          {/* <SubGraph className="result" no="2"/> */}
          <div className="result">
            결과값<br/><br/><br/><br/><br/>dfd<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
            </div>
          <MainGraph no="3"/>
        </article>
        <article className="filterContainer">
          <Filter no="1"/>
          <Filter no="2"/>
          <Filter no="3"/>
          <Filter no="3"/>
          <Filter no="3"/>
          <Filter no="3"/>
          <Filter no="3"/>
          <Filter no="3"/>
        </article>
      </section>
    </div>
  );
};

export default Dashboard;