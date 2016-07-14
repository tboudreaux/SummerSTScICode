from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[129.44675,19.832167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_J083747.22+194955.8/sdB_SDSSJ910_J083747.22+194955.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_J083747.22+194955.8/sdB_SDSSJ910_J083747.22+194955.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()