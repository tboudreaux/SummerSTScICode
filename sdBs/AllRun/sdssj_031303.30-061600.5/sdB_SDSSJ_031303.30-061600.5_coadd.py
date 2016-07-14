from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[48.26375,-6.266806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_031303.30-061600.5/sdB_SDSSJ_031303.30-061600.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_031303.30-061600.5/sdB_SDSSJ_031303.30-061600.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
