from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[340.718667,1.872931],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_2240+0136/sdB_HS_2240+0136_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_2240+0136/sdB_HS_2240+0136_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
