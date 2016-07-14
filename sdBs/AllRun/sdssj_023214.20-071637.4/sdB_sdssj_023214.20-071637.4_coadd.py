from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[38.059167,-7.277056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_023214.20-071637.4/sdB_sdssj_023214.20-071637.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_023214.20-071637.4/sdB_sdssj_023214.20-071637.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
