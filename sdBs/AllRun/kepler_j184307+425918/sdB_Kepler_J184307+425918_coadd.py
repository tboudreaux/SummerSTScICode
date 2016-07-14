from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[280.779167,42.988333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_J184307+425918/sdB_Kepler_J184307+425918_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_J184307+425918/sdB_Kepler_J184307+425918_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
