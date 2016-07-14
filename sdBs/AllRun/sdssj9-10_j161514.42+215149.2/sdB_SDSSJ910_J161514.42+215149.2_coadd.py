from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[243.810083,21.863667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_J161514.42+215149.2/sdB_SDSSJ910_J161514.42+215149.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_J161514.42+215149.2/sdB_SDSSJ910_J161514.42+215149.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()