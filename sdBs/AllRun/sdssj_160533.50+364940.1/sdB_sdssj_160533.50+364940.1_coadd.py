from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[241.389583,36.827806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_160533.50+364940.1/sdB_sdssj_160533.50+364940.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_160533.50+364940.1/sdB_sdssj_160533.50+364940.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
