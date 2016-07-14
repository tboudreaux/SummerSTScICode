from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[256.551792,25.708989],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_TON_266/sdB_TON_266_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_TON_266/sdB_TON_266_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
