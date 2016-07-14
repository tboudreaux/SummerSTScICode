from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[224.393333,3.799861],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_145734.40+034759.5/sdB_sdssj9-10_145734.40+034759.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_145734.40+034759.5/sdB_sdssj9-10_145734.40+034759.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
