from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[309.503917,4.485881],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_2035+0418/sdB_hs_2035+0418_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_2035+0418/sdB_hs_2035+0418_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
