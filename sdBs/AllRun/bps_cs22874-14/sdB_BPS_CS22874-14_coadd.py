from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[218.100667,-25.216469],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_BPS_CS22874-14/sdB_BPS_CS22874-14_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_BPS_CS22874-14/sdB_BPS_CS22874-14_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()