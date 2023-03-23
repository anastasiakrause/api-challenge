import React, { useEffect, useState } from "react";
import FastAPIClient from "../../client";
import config from "../../config";
import Header from "../../components/Header";
import Table from 'react-bootstrap/Table'

const client = new FastAPIClient(config);

const Dashboard = () => {
	const [vehicles, setVehicles] = useState([]);

	useEffect(() => {
		fetchVehicleData();
	}, []);

	const fetchVehicleData = () => {
		client.getVehicleData().then((data) => {
			setVehicles(data?.items);
		});
	};

	return (
		<>
			<section
				className="flex flex-col bg-white text-right"
				style={{ minHeight: "100vh" }}
			>
				<Header />
				<div className="container pt-20 text-left">
					<div>
						{vehicles.length}
						<Table striped bordered hover responsive="md">
							<thead>
								<tr>
									<th>Vehicle ID</th>
									<th>Timestamp</th>
									<th>Speed</th>
									<th>Odometer</th>
									<th>SOC</th>
									<th>Elevation</th>
									<th>Shift State</th>
								</tr>
							</thead>
							<tbody>
								<tr>
									<td>1</td>
									<td>Mark</td>
									<td>Otto</td>
									<td>@mdo</td>
									<td>hi</td>
									<td>hi</td>
									<td>hey</td>
								</tr>
							</tbody>
						</Table>
					</div>
				</div>
			</section>
		</>
	);
};

export default Dashboard;
