from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[290.29625,47.99],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_J19211+4759/sdB_Kepler_J19211+4759_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_J19211+4759/sdB_Kepler_J19211+4759_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
