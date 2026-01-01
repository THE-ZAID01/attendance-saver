function App() {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Attendance Saver</h1>
      <p style={styles.subtitle}>
        Smart Attendance Management System
      </p>

      <form style={styles.form}>
        <input placeholder="Student Name" style={styles.input} />
        <input placeholder="Roll Number" style={styles.input} />
        <input placeholder="Department" style={styles.input} />

        <button style={styles.button}>Add Student</button>
      </form>
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    background: "#0f172a",
    color: "#e5e7eb",
    fontFamily: "Arial",
  },
  title: {
    fontSize: "2.5rem",
    marginBottom: "0.5rem",
  },
  subtitle: {
    marginBottom: "2rem",
    color: "#94a3b8",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    width: "300px",
    gap: "12px",
  },
  input: {
    padding: "10px",
    borderRadius: "6px",
    border: "none",
    outline: "none",
  },
  button: {
    padding: "10px",
    borderRadius: "6px",
    border: "none",
    background: "#38bdf8",
    fontWeight: "bold",
    cursor: "pointer",
  },
};

export default App;
