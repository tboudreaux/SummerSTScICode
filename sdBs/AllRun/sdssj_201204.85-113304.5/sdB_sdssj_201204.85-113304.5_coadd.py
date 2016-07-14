from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[303.020208,-11.55125],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_201204.85-113304.5/sdB_sdssj_201204.85-113304.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_201204.85-113304.5/sdB_sdssj_201204.85-113304.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
