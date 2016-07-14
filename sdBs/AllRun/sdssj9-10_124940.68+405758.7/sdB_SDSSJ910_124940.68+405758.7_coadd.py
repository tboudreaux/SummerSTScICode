from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[192.4195,40.966306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_124940.68+405758.7/sdB_SDSSJ910_124940.68+405758.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_124940.68+405758.7/sdB_SDSSJ910_124940.68+405758.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
