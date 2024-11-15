import minergym.config as config
import minergym.query_info as query_info
import tests.test_data as test_data
import minergym.simulation as simulation
import minergym.data.building as building
import minergym.data.weather as weather


def test_full_config() -> None:

    obs_template = {}
    rdf = query_info.rdf_from_json(building.crawlspace)

    config.auto_add_temperature(rdf, obs_template)
    config.auto_add_energy(rdf, obs_template)

    sim = simulation.EnergyPlusSimulation(
        building.crawlspace,
        weather.honolulu,
        obs_template,
        {},
    )
    sim.start()
