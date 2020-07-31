import React from 'react';
// import Link from 'next/link';

const Filter = ({no}) => {
  return(
    <>
      <div className="filter">
          í•„í„° {no}
          <form>
            <div>
              <input type="checkbox"/>
              <span>list</span>
            </div>
            <div>
              <input type="checkbox"/>
              <span>list</span>
            </div>
            <div>
              <input type="checkbox"/>
              <span>list</span>
            </div>
          </form>
      </div>
    </>
  );
};

export default Filter;
