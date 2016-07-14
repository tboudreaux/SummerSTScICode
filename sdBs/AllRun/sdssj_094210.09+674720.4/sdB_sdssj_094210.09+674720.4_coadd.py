from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[145.542042,67.789],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_094210.09+674720.4/sdB_sdssj_094210.09+674720.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_094210.09+674720.4/sdB_sdssj_094210.09+674720.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
