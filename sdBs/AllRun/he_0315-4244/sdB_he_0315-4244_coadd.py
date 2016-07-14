from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[49.446292,-42.561442],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_0315-4244/sdB_he_0315-4244_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_0315-4244/sdB_he_0315-4244_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
