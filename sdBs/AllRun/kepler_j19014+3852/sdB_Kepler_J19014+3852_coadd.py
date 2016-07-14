from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[285.3575,38.875833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_J19014+3852/sdB_Kepler_J19014+3852_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_J19014+3852/sdB_Kepler_J19014+3852_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
