const TabList = ({ isShowCompleted, displayCompleted }) => {
  return (
    <div className="nav nav-tabs">
      <button type="button"
        onClick={() => displayCompleted(true)}
        className={isShowCompleted ? "nav-link active" : "nav-link"}
      >
        Complete
      </button>
      <button type="button"
        onClick={() => displayCompleted(false)}
        className={isShowCompleted ? "nav-link" : "nav-link active"}
      >
        Incomplete
      </button>
    </div>
  );
};

export default TabList;
