from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[240.845167,9.649833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_160322.84+093859.4/sdB_SDSSJ_160322.84+093859.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_160322.84+093859.4/sdB_SDSSJ_160322.84+093859.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
