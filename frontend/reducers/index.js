import { combineReducers } from 'redux';
import user from './user';
import group from './group';

const rootReducer =combineReducers({
    user,
    group,
});

export default rootReducer;