
const Teams = () => {
  const [teams, setTeams] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Teams endpoint:', endpoint);
        console.log('Fetched teams:', data);
        setTeams(Array.isArray(data) ? data : data.results || []);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, [endpoint]);

  return (
    <div className="card p-4 mb-4">
      <h2 className="mb-4 display-6">Teams</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead className="table-primary">
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>Members</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {teams.length === 0 ? (
              <tr><td colSpan="4" className="text-center">No teams found</td></tr>
            ) : (
              teams.map((team, idx) => (
                <tr key={idx}>
                  <td>{idx + 1}</td>
                  <td>{team.name || '-'}</td>
                  <td>{Array.isArray(team.members) ? team.members.length : '-'}</td>
                  <td>{team.description || '-'}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Teams;
