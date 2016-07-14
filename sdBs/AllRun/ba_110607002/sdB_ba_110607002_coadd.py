from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[185.952792,1.285667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ba_110607002/sdB_ba_110607002_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ba_110607002/sdB_ba_110607002_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
