import { combineReducers } from 'redux';
import user from './user';
import group from './group';
import lineYieldReducer from './lineYieldReducer';
import winRateReducer from './winRateReducer';
import capitalGrowthReducer from './capitalGrowthReducer';

const rootReducer =combineReducers({
    user,
    group,
    lineYieldReducer,
    winRateReducer,
    capitalGrowthReducer
});

export default rootReducer;