from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[353.5085,-28.860667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_TON_S103/sdB_TON_S103_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_TON_S103/sdB_TON_S103_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
