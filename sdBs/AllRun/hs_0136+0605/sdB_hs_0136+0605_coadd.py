from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[24.825042,6.35275],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_0136+0605/sdB_hs_0136+0605_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_0136+0605/sdB_hs_0136+0605_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
